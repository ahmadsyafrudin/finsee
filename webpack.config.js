const path = require("path");
const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const exclusions = /node_modules/;

module.exports = [
    {
        entry: {
            app: "./assets/js/app.js",
        },
        output: {
            path: path.resolve(__dirname, "finsee/static"),
            publicPath: "/static/",
            filename: "[name].js",
            chunkFilename: "[id]-[chunkhash].js",
        },
        devServer: {
            port: 8081,
            writeToDisk: true,
        },
        module: {
            rules: [
                {
                    test: /.*/,
                    include: path.resolve(__dirname, "assets/img"),
                    exclude: exclusions,
                    options: {
                        context: path.resolve(__dirname, "assets/"),
                        name: "[path][name].[ext]",
                    },
                    loader: "file-loader",
                },
                {
                    test: /\.riot$/,
                    exclude: /node_modules/,
                    use: [{
                        loader: '@riotjs/webpack-loader',
                        options: {
                            hot: false, // set it to true if you are using hmr
                            // add here all the other @riotjs/compiler options riot.js.org/compiler
                            // template: 'pug' for example
                        }
                    }]
                },
                {
                    test: /\.css$/,
                    exclude: exclusions,
                    use: [
                        MiniCssExtractPlugin.loader,
                        {loader: "css-loader"},
                    ],
                },
            ],
        },
        plugins: [
            new CleanWebpackPlugin({cleanStaleWebpackAssets: false}),
            new MiniCssExtractPlugin(),
        ],
    },
];
