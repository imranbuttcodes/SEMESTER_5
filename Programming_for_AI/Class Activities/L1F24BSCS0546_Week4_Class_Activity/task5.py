
def list_all_files(data):

    if isinstance(data, dict):
        for directory, contents in data.items():
            print(f"Directory: {directory}")
            list_all_files(contents)

    elif isinstance(data, list):
        for item in data:
            list_all_files(item)

    elif isinstance(data, str):
        print(f"-> File: {data}")


files = {
    "docs": [
        {"work": ["resume.pdf", "project.docx"]},
        {"personal": [
            {"pictures": ["photo.jpg", "vacation1.jpg", "vacation2.jpg"]},
            {"videos": []}
        ]},
        "todo.txt",
        "logfile.csv",
        {"downloads": []}
    ]
}

list_all_files(files)
