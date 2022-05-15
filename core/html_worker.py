from typing import List


def read_file(file_path: str) -> str:
    with open(file_path, "r") as reader:
        return reader.read()


def make_html(
    file_path: str,
    html_tag_values: None | str | List[str] = None,
    replace_inner: bool = True,
) -> str:
    html_text = read_file(file_path).lower()
    if html_tag_values is not None:
        if isinstance(html_tag_values, list):
            html_tag_values = "".join(html_tag_values)
        start_pos = html_text.index(">", html_text.index("<body")) + 1
        end_pos = html_text.index("</body")
        html_text = (4 * "{}").format(
            html_text[:start_pos],
            "" if replace_inner else html_text[start_pos:end_pos],
            html_tag_values,
            html_text[end_pos:],
        )
    return html_text


def erase_css(html_text: str) -> List[str]:
    html_text = html_text.lower()
    result: List[str] = []
    last_index = 0
    while True:
        try:
            pre_start_pos = html_text.index("<style", last_index)
            start_pos = html_text.index(">", pre_start_pos) + 1
            end_pos = html_text.index("</style")
            last_index = end_pos
            result.append(html_text[start_pos:end_pos])
        except ValueError:
            break
    return result
