// const path = require('path');

// module.exports = {
//   entry: './src/index.js', // Update this based on your entry file
//   output: {
//     filename: 'bundle.js',
//     path: path.resolve(__dirname, 'dist'),
//   },
//   module: {
//     rules: [
//       {
//         test: /\.js$/,
//         exclude: /node_modules/,
//         use: {
//           loader: 'babel-loader',
//           options: {
//             presets: ['@babel/preset-env'],
//           },
//         },
//       },
//     ],
//   },
//   resolve: {
//     fallback: {
//       "zlib": require.resolve("browserify-zlib"),
//       "querystring": require.resolve("querystring-es3"),
//       "path": require.resolve("path-browserify"),
//       "buffer": require.resolve("buffer/"),
//       "crypto": require.resolve("crypto-browserify"),
//       "stream": require.resolve("stream-browserify"),
//       "util": require.resolve("util/"),
//       "http": false,
//       "fs": false, // This is to handle 'fs' module, you can add more as needed
//       "net": false, // Add this line for the 'net' module
//     }
//   }
// };
