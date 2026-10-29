def clean(docs):
    clean_text = '\n\n'.join(doc.page_content for doc in docs)
    return clean_text


def clean_search_tool_result(results):
    search_text = "\n\n".join(
                    f"Title: {item.get('title', '')}\n"
                    f"Snippet: {item.get('snippet', '')}\n"
                    f"URL: {item.get('link', '')}"
                    for item in results.get("organic", [])
        )
    return search_text