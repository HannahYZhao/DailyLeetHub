/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let myMap = new Map();
    strs.forEach((ele)=>{
        let eleSorted = ele.split('').sort().join('');
        if(myMap.has(eleSorted)){
            myMap.set(eleSorted , [ele, ...myMap.get(eleSorted)])
        }
        else
        myMap.set(eleSorted , [ele])
    })
    return (Array.from(myMap.values()))

};