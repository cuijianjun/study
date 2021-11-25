function add (x:number, y:number, z?:number):number {
  return x + y
}

interface ISum {
  (x: number, y: number, z?: number): number
}

let add2: ISum = add