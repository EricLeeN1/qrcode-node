const fs = require("fs");
const jsQR = require("jsqr");
const { Jimp } = require("jimp");
const path = require("path");
const directoryPath = "./images"; // 替换为您的图片目录路径
console.log(Jimp);
let txtArr = [];

const removeProtocol = (url) => {
  // 定义正则表达式，匹配 http:// 或 https://
  const regex = /^(http:\/\/|https:\/\/|ftp:\/\/)/;

  // 使用 replace 方法替换匹配到的部分为空字符串
  const cleanedUrl = url.replace(regex, "");

  return cleanedUrl;
};

fs.readdir(directoryPath, (err, files) => {
  //   console.log(files);

  if (err) {
    return console.log("Unable to scan directory: " + err);
  }

  // 过滤出图片文件
  files = files.filter((file) => {
    const extension = file.split(".").pop();
    const imageExtensions = ["jpg", "jpeg", "png", "gif", "bmp"]; // 可以根据需要添加或删除图片格式
    return imageExtensions.includes(extension);
  });

  // 读取图片信息
  files.forEach(async (file) => {
    const filePath = path.join(directoryPath, file);
    try {
      const imgData = fs.readFileSync(filePath);
      const { bitmap } = await Jimp.read(imgData);
      const { data } = jsQR(bitmap.data, bitmap.width, bitmap.height);
      console.log(data,filePath);
      
      txtArr.push(`https://h5.clewm.net/?url=${removeProtocol(data)}`);
      if (txtArr.length == files.length) {
        console.log(txtArr);
        const jsonDatas = {
          name: "药品地址列表",
          lists: txtArr,
        };
        const jsonStr = JSON.stringify(jsonDatas);
        try {
          fs.writeFileSync("./data.json", jsonStr);
          console.log("JSON data written to file successfully.");
        } catch (err) {
          console.error("Error writing JSON data to file:", err);
        }
      }
    } catch (error) {
      console.log("Error stating file:", filePath);
    }
  });
});
