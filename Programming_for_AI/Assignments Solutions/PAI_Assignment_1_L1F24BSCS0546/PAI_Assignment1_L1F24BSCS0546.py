
import csv
import time


def timer(func):

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        print(
            f"\nTime taken to find records: "
            f"{end_time - start_time:.4f} seconds"
        )

        return result

    return wrapper


# --- TASK 1: THE SCP DECODER ---
def get_mi_mapping(mapping_csv_path):
    mi_map = {}

    with open(mapping_csv_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames

        for row in reader:
            if row[fields[7]] == "Myocardial Infarction":
                mi_map[row[fields[0]]] = row["description"]

    return mi_map


# --- TASK 2: THE PATIENT GENERATOR ---
def mi_patient_generator(database_csv_path, mi_mapping):
    with open(database_csv_path, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            scp_codes = row["scp_codes"]

            for code in mi_mapping:
                if f"'{code}'" in scp_codes:
                    yield {
                        "patient_id": row["patient_id"],
                        "age": row["age"],
                        "sex": row["sex"],
                        "record_date": row["recording_date"],
                        "diagnosis": mi_mapping[code],
                        "filename": row["filename_hr"]
                    }
                    break


# --- TASK 3: EXECUTION & TIMING ---
@timer
def main():
    db_path = "ptbxl_database.csv"
    statements_path = "scp_statements.csv"

    print("--- Initializing MI Mapping ---")
    mi_mapping = get_mi_mapping(statements_path)

    print(f"Loaded {len(mi_mapping)} MI-related diagnostic codes.\n")
    print("--- Starting Patient Stream ---")

    count = 0

    for patient in mi_patient_generator(db_path, mi_mapping):
        print(patient)
        count += 1

        if count == 25:
            break


if __name__ == "__main__":
    main()
