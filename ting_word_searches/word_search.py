def exists_word(word, instance):
    result = []

    for index in range(len(instance)):
        file = instance.search(index)

        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1}
                for index, line in enumerate(file["linhas_do_arquivo"])
                if word in line.lower()
            ],
        }

        if data["ocorrencias"]:
            result.append(data)
        else:
            []

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
