def categorize_student_records(ids, scores):

    result = {
        id: {
            "score": score,
            'tier': "Distinction" if score >= 85 else 
            "Satisfactory" if 60 <= score < 78  else 
            "Remedial" 
        }
        
        for id, score in zip(ids, scores)
    }

    return result

print(categorize_student_records(["ST_101", "ST_102", "ST_103", "ST_104", "ST_105"], [92, 45, 78, 58, 81]))