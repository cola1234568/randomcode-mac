echo "Where do you want to risk?"
read -p "Please use forward slashes (/) and not backslashes (\). > " path

function file_set() {
  if [ ! -d "$1" ]; then
    echo "$1 doesn't exist. Please choose a valid path"
    exit 1
  fi
  local path_list=($(ls "$1"))
  if [ ${#path_list[@]} -eq 0 ]; then
    echo "No files in the specified directory. Exiting..."
    exit 1
  fi
  local set_file=${path_list[$RANDOM % ${#path_list[@]}]}
  echo $set_file
}

file_to_delete=$(file_set $path)
read -p "Press enter to shoot $file_to_delete, or type any letter to quit > " shoot
if [ -n "$shoot" ]; then
    echo "Exiting..."
    exit
fi

while true; do
  if [ $((RANDOM % 7)) -eq 2 ]; then
    echo "Unlucky...deleting $file_to_delete"
