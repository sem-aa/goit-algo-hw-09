const sum = 113
const monets = [50, 25, 10, 5, 2, 1]

const findCoinsGreedy = (sum, monets) => {
    const obj = {}
    let greedy = sum
    console.log(greedy);
    
    while (greedy > 0) {
        monets.forEach(element => {
            
            if (element <= sum) {
                if (!obj[element]) {
                    obj[element] = 1
                } else obj[element] += 1

                greedy -= element
           
            }
            
        });
    }
  
    return obj
}

findCoinsGreedy(sum, monets)

