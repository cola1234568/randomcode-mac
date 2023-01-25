echo "Select Rock, Paper, or Scissors to play!"
echo "Player:"
read pInput

choices=("rock" "paper" "scissors")
while ! [[ " ${choices[@]} " =~ " ${pInput} " ]]; do
  echo "Please try again"
  echo "type rock, paper, or scissors to play."
  echo "Player:"
  read pInput
done

cInput=$(shuf -n1 -e ${choices[@]})
echo "Computer: ${cInput^}"

function checkMoves() {
  local pi=$1
  local ci=$2
  local currentMatch="${pi} vs. ${ci}"
  if [ "$pi" == "$ci" ]; then
    echo "${currentMatch} is a draw!"
  elif [ "$pi" == "Rock" ]; then
    if [ "$ci" == "Scissors" ]; then
      echo "${currentMatch}, You win!"
    elif [ "$ci" == "Paper" ]; then
      echo "${currentMatch}, Computer wins!"
    fi
  elif [ "$pi" == "Paper" ]; then
    if [ "$ci" == "Rock" ]; then
      echo "${currentMatch}, You win!"
    elif [ "$ci" == "Scissors" ]; then
      echo "${currentMatch}, Computer wins!"
    fi
  elif [ "$pi" == "Scissors" ]; then
    if [ "$ci" == "Paper" ]; then
      echo "${currentMatch}, You win!"
    elif [ "$ci" == "Rock" ]; then
      echo "${currentMatch}, Computer wins!"
    fi
  fi
}

checkMoves "$pInput" "$cInput"
