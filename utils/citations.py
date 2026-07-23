def format_citations(citations):
    """
    Remove duplicate citations and format them.
    """

    seen = set()

    formatted = []

    for item in citations:

        key = (
            item["source"],
            item["page"],
            item["chunk"]
        )

        if key in seen:
            continue

        seen.add(key)

        formatted.append(
            f"📄 {item['source']} | "
            f"Page {item['page']} | "
            f"Chunk {item['chunk']}"
        )

    return formatted