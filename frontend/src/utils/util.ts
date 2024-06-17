export const getAssetsFile = (dirName: string, fileName: string): string => {
    const url = new URL(`../assets/${dirName ? dirName + '/' : ''}${fileName}`, import.meta.url).href
    return url
}