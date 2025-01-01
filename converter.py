import re

def parse_questionnaire(input_text):
    try:
        lines = input_text.strip().split("\n")
        html_output = []
        js_validations = []
        question_index = 1  # 用于区分每个问题的ID

        lines_iter = iter(lines)
        for line in lines_iter:
            line = line.strip()

            # 标题处理
            if line.startswith("[#]"):
                title = re.sub(r"\[#\]|\[\*\*](.*?)\[\*\*]", r"<b>\1</b>", line[3:])
                html_output.append(f"<h2>{title}</h2>")

            # 必填或非必填处理
            elif "[*]" in line or "[/]" in line:
                required = "[*]" in line
                is_optional = "[/]" in line
                line = line.replace("[*]", "").replace("[/]", "")

                # 单选或多选
                if "[&=" in line:
                    count = int(re.search(r"\[&=(\d+)\]", line).group(1))
                    question_text = line.split('[&=')[0].strip()  # 获取问题的主要部分
                    remaining_text = re.sub(r".*\[&=\d+\]", "", line).strip()  # 获取标记后面的文字
                    html_output.append(f"<p>{question_text} {remaining_text}</p>")
                    # html_output.append(f"<p>{line.split('[&=')[0].strip()}</p>")
                    options = []
                    option_index = 1
                    while True:
                        try:
                            option_line = next(lines_iter).strip()
                            if option_line == "---":
                                break
                            input_type = "radio" if count == 1 else "checkbox"
                            options.append(f'<input type="{input_type}" name="question_{question_index}" value="{option_line}" id="q{question_index}_opt{option_index}"> <label for="q{question_index}_opt{option_index}">{option_line}</label><br>')
                            option_index += 1
                        except StopIteration:
                            break
                    html_output.extend(options)
                    if required:
                        if count == 1:
                            js_validations.append(f"""
                            var selected = document.querySelector('input[name="question_{question_index}"]:checked');
                            if (!selected) {{
                                alert("请选择一个选项。");
                                return false;
                            }}
                            """)
                        else:
                            js_validations.append(f"""
                            var selected = document.querySelectorAll('input[name="question_{question_index}"]:checked').length;
                            if (selected != {count}) {{
                                alert("请选择 {count} 个选项。");
                                return false;
                            }}
                            """)
                    question_index += 1

                # 填空题
                elif "[~=" in line:
                    x, y = map(int, re.search(r"\[~=(\d+),(\d+)\]", line).groups())
                    question_text = line.split("[~=")[0].strip()
                    remaining_text = re.sub(r".*\[~=\d+,\d+\]", "", line).strip()
                    html_output.append(f'<label>{question_text} {remaining_text}</label><br>')
                    # html_output.append(f'<label>{line.split("[~=")[0].strip()}</label><br>')
                    html_output.append(f'<input type="text" id="q{question_index}" name="question_{question_index}" maxlength="{y}" minlength="{x}"><br>')
                    if required:
                        js_validations.append(f"""
                        var input = document.getElementById("q{question_index}").value;
                        if (input.length < {x}) {{
                            alert("该项必须输入至少 {x} 个字符。");
                            return false;
                        }}
                        """)
                    question_index += 1

                # 问答题
                elif "[_=" in line:
                    x, y = map(int, re.search(r"\[_=(\d+),(\d+)\]", line).groups())
                    question_text = line.split("[_=")[0].strip()
                    remaining_text = re.sub(r".*\[_=\d+,\d+\]", "", line).strip()
                    html_output.append(f'<label>{question_text} {remaining_text}</label><br>')
                    # html_output.append(f'<label>{line.split("[_=")[0].strip()}</label><br>')
                    html_output.append(f'<textarea id="q{question_index}" name="question_{question_index}" maxlength="{y}" minlength="{x}"></textarea><br>')
                    if required:
                        js_validations.append(f"""
                        var input = document.getElementById("q{question_index}").value;
                        if (input.length < {x}) {{
                            alert("该项必须输入至少 {x} 个字符。");
                            return false;
                        }}
                        """)
                    question_index += 1

                # 日期选项
                elif "[%=" in line:
                    format_type = re.search(r"\[%=(.*?)\]", line).group(1)
                    question_text = line.split("[%=")[0].strip()
                    remaining_text = re.sub(r".*\[%=.*?\]", "", line).strip()
                    html_output.append(f"<p>{question_text} {remaining_text}</p>")
                    
                    if format_type == "md":
                        html_output.append(f'<select id="q{question_index}_month"><option value="">Month</option>{"".join([f"<option value={i}>{m}</option>" for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], 1)])}</select>')
                        html_output.append(f'<select id="q{question_index}_day"><option value="">Day</option>{"".join([f"<option value={i}>{i}</option>" for i in range(1, 32)])}</select><br>')
                        if required:
                            js_validations.append(f"""
                            var month = document.getElementById("q{question_index}_month").value;
                            var day = document.getElementById("q{question_index}_day").value;
                            if (!month || !day) {{
                                alert("请选择完整的日期。");
                                return false;
                            }}
                            """)
                    elif format_type == "y":
                        html_output.append(f'<label for="q{question_index}_year"></label>')
                        html_output.append(f'<input type="number" id="q{question_index}_year" name="question_{question_index}"><br>')
                        if required:
                            js_validations.append(f"""
                            var year = document.getElementById("q{question_index}_year").value;
                            if (!year) {{
                                alert("请输入出生年份。");
                                return false;
                            }}
                            """)
                    question_index += 1


                # 邮箱填空
                elif "[@]" in line:
                    html_output.append(f'<label>{line.replace("[@]", "").strip()}</label><br>')
                    html_output.append(f'<input type="email" id="q{question_index}" name="question_{question_index}"><br>')
                    if required:
                        js_validations.append(f"""
                        var email = document.getElementById("q{question_index}").value;
                        var email_pattern = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
                        if (!email_pattern.test(email)) {{
                            alert("请输入有效的邮箱地址。");
                            return false;
                        }}
                        """)
                    question_index += 1

        # 生成HTML
        html_body = "\n".join(html_output)
        js_script = "\n".join(js_validations)
        html_final = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>PolarForm</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='survey_styles.css') }}">
            <script>
                function submitForm() {{
                    {js_script}
                    alert("问卷提交成功！");
                }}
            </script>
        </head>
        <body>
            <header>
                <img src="{{ url_for('static', filename='logo.png') }}" alt="ACS Studio Logo" id="logo">
                <h1>PolarForm - By ACS Studio</h1>
                <p>Discover Data with Polar Precision</p>
            </header>

            <nav>
                <ul>
                    <li><a href="https://acsstudio.site/">Home</a></li>
                    <li><a href="https://acsstudio.site/avp/">AVP</a></li>
                </ul>
            </nav>

            <section>
                <form onsubmit="return submitForm();">
                {html_body}
                <button type="submit">提交问卷</button>
                </form>   
            </section>

            <footer>
                <p>© 2024 ACS Studio - Air Maple Studio. All rights reserved.</p>
            </footer>
        </body>
        </html>
        """
        # with open("questionnaire.html", "w", encoding="utf-8") as f:
        #     f.write(html_final)
        
    except Exception as e:
        return [False,html_final]
    else:
        return [True,html_final]
