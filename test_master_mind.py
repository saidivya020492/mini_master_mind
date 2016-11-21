import pytest
from SecretCode import *
from InputHandler import *
from Game import *


def test_store_secret_code():
    ret_val, err_msg = SecretCode().store_secret_code("PBGY")
    assert ret_val == True

def test_store_secret_code_shorter_length():
    ret_val,err_msg = SecretCode().store_secret_code("PBG")
    assert ret_val==False
    assert  err_msg ==  "INPUT Should be of length 4 !!"

def test_store_secret_code_larger_length():
    ret_val, err_msg = SecretCode().store_secret_code("PBGGGGG")
    assert ret_val == False
    assert err_msg == "INPUT Should be of length 4 !!"

def test_store_secret_code_duplicate_colors():
    ret_val, err_msg = SecretCode().store_secret_code("PBGG")
    assert ret_val == False
    assert err_msg ==  "INPUT contains Dulpicate colors : ['G']"

def test_store_secret_code_invalid_color():
    ret_val, err_msg = SecretCode().store_secret_code("PBGX")
    assert ret_val == False
    assert err_msg == "INVALID color Selected : X\n !! Pls Select from  : ['P', 'B', 'G', 'Y', 'R', 'O']"

def test_store_secret_code_empty_code():
    ret_val, err_msg = SecretCode().store_secret_code("")
    assert ret_val == False
    assert err_msg == "INPUT Should be of length 4 !!"


def test_store_input_attempt():
    ret_val, err_msg = InputHandler().store_input_attempt("PBGY")
    assert ret_val == True

def test_store_input_attempt_shorter_length():
    ret_val,err_msg = InputHandler().store_input_attempt("PBG")
    assert ret_val==False
    assert  err_msg ==  "INPUT Should be of length 4 !!"

def test_store_input_attempt_larger_length():
    ret_val, err_msg = InputHandler().store_input_attempt("PBGGGGG")
    assert ret_val == False
    assert err_msg == "INPUT Should be of length 4 !!"

def test_store_input_attempt_duplicate_colors():
    ret_val, err_msg = InputHandler().store_input_attempt("PBGG")
    assert ret_val == False
    assert err_msg ==  "INPUT contains Dulpicate colors : ['G']"

def test_store_input_attempt_invalid_color():
    ret_val, err_msg = InputHandler().store_input_attempt("PBGX")
    assert ret_val == False
    assert err_msg == "INVALID color Selected : X\n !! Pls Select from  : ['P', 'B', 'G', 'Y', 'R', 'O']"

def test_store_input_attempt_empty_code():
    ret_val, err_msg = InputHandler().store_input_attempt("")
    assert ret_val == False
    assert err_msg == "INPUT Should be of length 4 !!"


def test_tally_with_secret_code_valid_case():
    game_obj=Game()
    game_obj.secret_code = "PBGY"
    attempt_res,attempt_msg,attempt_suggestion=game_obj.tally_with_secret_code("PBGY")
    assert attempt_res == True
    assert  attempt_msg == "You won the game!!!"


def test_tally_secret_code_with_attempt_001():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("RGYB")
    assert attempt_res == False
    assert attempt_msg == "\nBlacks  : 0\nWhites  : 3\nNoColor : 1"


def test_tally_secret_code_with_attempt_002():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("PGYB")
    assert attempt_res == False
    assert attempt_msg == "\nBlacks  : 1\nWhites  : 3\nNoColor : 0"

def test_tally_secret_code_with_attempt_003():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("BPYG")
    assert attempt_res == False
    assert attempt_msg == "\nBlacks  : 0\nWhites  : 4\nNoColor : 0"

def test_tally_secret_code_with_attempt_004():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("PBYG")
    assert attempt_res == False
    assert attempt_msg == "\nBlacks  : 2\nWhites  : 2\nNoColor : 0"

def test_tally_secret_code_with_attempt_005():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("PBGO")
    assert attempt_res == False
    assert attempt_msg == "\nBlacks  : 3\nWhites  : 0\nNoColor : 1"

def test_tally_secret_code_with_attempt_006():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("PBOG")
    assert attempt_res == False
    assert attempt_msg == "\nBlacks  : 2\nWhites  : 1\nNoColor : 1"

def test_tally_secret_code_with_attempt_007():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("PBGO")
    assert attempt_res == False
    assert attempt_msg == "\nBlacks  : 3\nWhites  : 0\nNoColor : 1"

def test_tally_secret_code_with_attempt_008():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("BPYO")
    assert attempt_res == False
    assert attempt_msg == "\nBlacks  : 0\nWhites  : 3\nNoColor : 1"

def test_tally_secret_code_with_attempt_009():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("PBRO")
    assert attempt_res == False
    assert attempt_msg == "\nBlacks  : 2\nWhites  : 0\nNoColor : 2"

def test_tally_secret_code_with_attempt_010():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("BPRO")
    assert attempt_res == False
    assert attempt_msg == "\nBlacks  : 0\nWhites  : 2\nNoColor : 2"


def test_tally_secret_code_with_attempt_011():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg,attempt_suggestion = game_obj.tally_with_secret_code("PYRO")
    assert attempt_res == False


def test_suggestion_attempting_same_code_001():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    dont_care_res = game_obj.tally_with_secret_code("PGYR")
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("PGYR")
    assert attempt_suggestion == "\nHey !! this combination was already attempted!! in attempt1"

def test_suggestion_attempting_same_code_002():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    dont_care_res = game_obj.tally_with_secret_code("BPYG")
    dont_care_res = game_obj.tally_with_secret_code("BPYO")
    dont_care_res = game_obj.tally_with_secret_code("BPYR")
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("BPYG")
    assert attempt_suggestion == "\nHey !! this combination was already attempted!! in attempt1\n!! You are almost there try swapping colors"

def test_suggestion_attempting_same_code_003():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    dont_care_res = game_obj.tally_with_secret_code("PGYO")
    dont_care_res = game_obj.tally_with_secret_code("PGYR")
    dont_care_res = game_obj.tally_with_secret_code("PBYR")
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("PGYR")
    assert attempt_suggestion == "\nHey !! this combination was already attempted!! in attempt2"
"""
def test_suggestion_missing_colors1():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("PBRO")
    assert attempt_suggestion == "\nYou  can try  from these colors : ['Y', 'G']"


def test_suggestion_missing_colors2():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("BPYO")
    assert attempt_suggestion == "\nYou  can try  from these colors : ['R', 'G']"
"""
def test_suggestion_swapping():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("BPYG")
    assert attempt_suggestion == "\n!! You are almost there try swapping colors"

def test_suggestion_swapping():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("PBYG")
    assert attempt_suggestion == "\n!! You are almost there try swapping colors"

def test_suggestion_swapping():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("PGYB")
    assert attempt_suggestion == "\n!! You are almost there try swapping colors"

def test_suggestion_one_position_with_no_match_001():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("PBGO")
    assert attempt_suggestion == "\n!! You Nailed Three Positions try a different color"

def test_suggestion_one_position_with_no_match_002():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("PBOY")
    assert attempt_suggestion == "\n!! You Nailed Three Positions try a different color"

def test_suggestion_one_position_with_no_match_003():
    game_obj = Game()
    game_obj.secret_code = "PBGY"
    attempt_res, attempt_msg, attempt_suggestion = game_obj.tally_with_secret_code("POGY")
    assert attempt_suggestion == "\n!! You Nailed Three Positions try a different color"








