class Queue<T> {
  private data = [];
  push(item: T) {
    return this.data.push(item)
  }
  pop():T{
    return this.data.shift()
  }
}

const queue = new Queue<number>()
queue.push(1)
console.log(queue.pop().toFixed())

interface Keypair<T, U> {
  key: T
  value: U
}

let kp1: Keypair<number, String> = {
  key:1,
  value: 'string'
}

let kp2: Keypair<string,number> = {
  key: 'str',
  value: 2
}

let arr:number[] = [1,2,3]
let arrTwo:Array<number> = [1,2,3]