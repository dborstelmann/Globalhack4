module.exports = function(grunt) {
    require('jit-grunt')(grunt);

    grunt.initConfig({
        concat: {
            options: {
                separator: ';\n\n',
            },
            dist: {
                src: ['js/vendor/*.js', 'js/templates.js', 'js/src/*.js'],
                dest: 'dist/build.js'
            },
            css: {
                src: ['css/*.css'],
                dest: 'dist/build.css'
            }
        },
        less: {
            development: {
                options: {
                    compress: true,
                    yuicompress: true,
                    optimization: 2
                },
                files: {
                    "css/main.css": "less/**/*.less" // destination file and source file
                }
            }
        },
        watch: {
            styles: {
                files: ['js/**/*,js', 'less/**/*.less', 'css/*.css', 'templates/**/*.html'], // which files to watch
                tasks: ['less', 'template-module', 'concat'],
                options: {
                    nospawn: true
                }
            }
        },
        'template-module': {
            compile: {
                options: {
                    module: false,
                    provider: 'underscore',
                    processName: function(filename){
                        return filename.replace(/^templates\//, '').replace(/\.html$/, '');
                    }
                },
                files: {
                    "js/templates.js": ["templates/**/*.html"]
                }
            }
    }
    });

    grunt.registerTask('default', ['less', 'template-module', 'concat', 'watch']);
};
