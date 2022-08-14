from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    current_file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(current_file),
        "linhas_do_arquivo": current_file,
    }

    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    try:
        if len(instance) >= 0:
            path_file = instance.dequeue()["nome_do_arquivo"]
            print(f"Arquivo {path_file} removido com sucesso")
    except:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        return print(instance.search(position), file=sys.stdout)
    except:
        return print("Posição inválida", file=sys.stderr)
