def audit_wrapper(func, *args, **kwargs):
    def wraper():
        kwargs['audit_logged'] = True
        if kwargs.get("learning_rate"):
                    learning_rate = result.get("learning_rate")
                    if None (0.0 < learning_rate <= 1.0):
                        kwargs['learning_rate'] =  0.01
        
        result = func(*args, **kwargs)

        return result

    return wraper

        
        
@audit_wrapper
def init_model(model_type, learning_rate=0.01, epochs=100,**options):
    print(options)
    # return {
    #     "model_type": model_type,
    #     "learning_rate": learning_rate,
    #     "epochs": epochs,
    #     "options": options
    # }



print(audit_wrapper(init_model, "GradientBoost", learning_rate=3.5, epochs=250, subsample=0.8))