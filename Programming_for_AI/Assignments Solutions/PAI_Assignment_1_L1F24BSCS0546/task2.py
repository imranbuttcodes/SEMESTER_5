import csv


def mi_patient_streamer(csv_path, mapping_dict):
    with open(csv_path) as file:
        reader = csv.DictReader(file)

        for row in reader:
            scp_codes = row['scp_codes']

            matching_codes = [
                code for code in mapping_dict
                if code in scp_codes
            ]


            if matching_codes:
                code = matching_codes[0]

                yield {
                    "patient_id": row["patient_id"],
                    "age": row["age"],
                    "sex": row["sex"],
                    "record_date": row["recording_date"],
                    "diagnosis": mapping_dict[code],
                    "filename": row["filename_hr"]
                }





