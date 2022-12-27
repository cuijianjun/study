export default (enforce?: 'pre'|'post') => {
    return {
        name: 'test',
        enforce,
        buildStart() {
            console.log("buildStart", enforce);
        },
        resolved() {
            console.log('resolveId', enforce);
        },
        load() { 
            console.log('load', enforce);
        }
    }
}