def exists_word(word, instance):
    search = search_by_word(word, instance)

    if len(search):
        return [
            {
                "palavra": result["palavra"],
                "arquivo": result["arquivo"],
                "ocorrencias": [
                    {"linha": occurrences["linha"]}
                    for occurrences in result["ocorrencias"]
                ],
            }
            for result in search
        ]

    return search


def search_by_word(word, instance):
    result = []

    for index in range(len(instance)):
        file = instance.search(index)

        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1, "conteudo": line}
                for index, line in enumerate(file["linhas_do_arquivo"])
                if word in line.lower()
            ],
        }

        if data["ocorrencias"]:
            result.append(data)
        else:
            []

    return result
