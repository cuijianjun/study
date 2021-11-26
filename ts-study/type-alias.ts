let sum:(x:number, y:number) => number
const result1 = sum(1,2)
type PlusType = (x:number, y:number) => number
let sum2:PlusType
const result3 = sum2(2,3)
type StrOrNumber = string | number
let result4: StrOrNumber = "123"
result4 = 123

const str: "name" = "name"
const number:1 = 1
type Directions = "Up" | "Down"|"Left"|"Right"
let toWhere:Directions = "Left"

