const fs = require("fs");
const jsQR = require("jsqr");
const { Jimp } = require("jimp");
const path = require("path");
const directoryPath = "./images"; // 替换为您的图片目录路径
console.log(Jimp);
let txtArr = [];
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
  files.forEach((file) => {
    const filePath = path.join(directoryPath, file);
    fs.readFile(filePath, async (err, imgData) => {
      if (err) {
        console.log("Error stating file:", filePath);
        return;
      }
      const { bitmap } = await Jimp.read(imgData);
      //   console.log(bitmap);

      const { data } = jsQR(bitmap.data, bitmap.width, bitmap.height);
      //   console.log(data);
      txtArr.push(data);
      //   console.log(bitmap.width, bitmap.height); // 打印文件名和大小
      console.log(txtArr);
    });
  });
  console.log(txtArr);
});
