function fizzbuzz(range){
    var newstr = ''
    
    for (let i = 0; i < range; i++) {
        if (i % 5 === 0 || i % 3 === 0) {
            if (i % 5 === 0) {
                newstr += "Fizz"
            }
            if (i % 3 === 0) {
                newstr += "Buzz"
            }
            console.log(newstr)
            newstr = ''
        } else {
            console.log(i)
        }
    }
}


fizzbuzz(100)
// could definitely use some refining here.
