#define function
def arithmetic_arranger(problems, show_answer):
  #initialize variables
  arranged_problems = ""
  lines = ["","","",""]
  num_problems = len(problems)

  #take 5 problems max
  if num_problems <= 5:
    #loop through each problem
    for problem in problems:
      #split it based on whitespace
      num1, operator, num2 = problem.split()

      #check if operator is + or - and, if not, return error
      if operator == "+":
        answer = str(int(num1) + int(num2))
      elif operator == "-":
        answer = str(int(num1) - int(num2))
      else:
        return str("Error: Please only use addition (+) and subtraction (-).")
        break

      #set the width of the problem to the longer number and check if it
      #is longer than four digits
      width = max(len(num1), len(num2)) + 2
      if(width - 2 > 4):
        return str("Error: Please only input numbers that are 4 digits max.")
        break

      #create the lines
      lines[0] += num1.rjust(width) + "    "
      lines[1] += operator + " " + num2.rjust(width - 2) + "    "
      lines[2] += "-" * width + "    "

      #if show_answer is true, add an extra line with the answer
      if show_answer:
        lines[3] += answer.rjust(width) + "    "

      #join all the lines into arranged_problems
      arranged_problems = "\n".join(lines)
    #return to function
    return arranged_problems  

  #handle situation where there is more than 5 problems
  else:
    return str("Error: Please enter, at most, 5 problems.")
