count_vowels() {
    s=$1
    vowels="aeiou"
    count=0
    for ((i=0; i<${#s}; i++)); do
        if [[ $vowels =~ ${s:$i:1} ]]; then
            count=$((count + 1))
        fi
    done
    echo $count
}
