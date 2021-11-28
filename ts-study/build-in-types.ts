const a:Array<number> = [1,2,3]
const date = new Date()
date.getTime()

const reg = /abc/
reg.test('abc')

let body = document.body
let allLis = document.querySelectorAll('li')
allLis.keys()

document.addEventListener('click', (e) => {
  e.preventDefault()
})


let viking: IPerson = {name: 'viking', age: 20}

type IPartial = Partial<IPerson>

let viking2: IPartial = {name: 'viking'}

type IOmit = Omit<IPerson, "name">
let viking3: IOmit = {
  age: 20
}
