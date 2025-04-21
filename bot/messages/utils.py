def format_telegram_table(headers, rows):
    """
    Формирует ASCII‑таблицу с разделителями '|' и выравниванием по ширине.
    Возвращает строку с обёрткой в ```…``` для отправки через MarkdownV2.

    :param headers: список заголовков колонок, например ['Кол1', 'Кол2', 'Кол3']
    :param rows: список строк, каждая строка — список значений, например [['A','B','C'], ['D','E','F']]
    :return: строка вида:
    ```markdown
    ```
    | Кол1 | Кол2 | Кол3 |
    |------|------|------|
    | A    | B    | C    |
    | D    | E    | F    |
    ```
    """
    # Считаем ширину каждой колонки
    cols = len(headers)
    # максимальная ширина в каждой колонке среди заголовка и всех строк
    widths = [len(str(headers[i])) for i in range(cols)]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    # собираем строку с заголовками
    header_line = "| " + " | ".join(str(headers[i]).ljust(widths[i]) for i in range(cols)) + " |"
    # разделитель
    sep_line = "|-" + "-|-".join("-" * widths[i] for i in range(cols)) + "-|"

    # собираем все строки данных
    row_lines = []
    for row in rows:
        row_line = "| " + " | ".join(str(row[i]).ljust(widths[i]) for i in range(cols)) + " |"
        row_lines.append(row_line)

    # объединяем всё вместе
    table = "\n".join([header_line, sep_line] + row_lines)

    # обёртываем в MarkdownV2 тройными бэктиками
    return f"```\n{table}\n```"

