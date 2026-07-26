def set_previous_result(state, value):
    state["previous_result"] = value

state = {"previous_result": None, "reuse_result": False}

set_previous_result(state, None)

print(state["previous_result"])   # 40


