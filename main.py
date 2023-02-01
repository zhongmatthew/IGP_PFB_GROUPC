# import other files as modules
import coh, overheads, profit_loss

# use "def" to create a main function to modularize the programn
def main():
    """
    - Function calls and execute each function from different files
    """
    
    # from each module, orderly call and execute each function 
    overheads.overhead()
    coh.coh()
    profit_loss.profitloss()

# call "main" function and execute
main()

# ----------------- Base solution ----------------- #
# import coh, overheads, profit_loss

# def main():
#     """
#     - Function calls and execute each function from different files
#     """

#     overheads.overhead()
#     coh.coh()
#     profit_loss.profitloss()

# main()