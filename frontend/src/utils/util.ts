
export const getAssetsFile = (dirName:string,fileName:string):string => {
    let url = `../assets/${dirName ? dirName + '/' : ''}${fileName}`
    return new URL(url,import.meta.url).toString()
}