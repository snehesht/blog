/**
 * Install:
 * $ npm install gulp gulp-minify-css gulp-autoprefixer gulp-ruby-sass gulp-coffee gulp-uglify gulp-concat gulp-rimraf gulp-notify
 */
const gulp = require('gulp');

// styles
const minifycss = require('gulp-minify-css');
const autoprefixer = require('gulp-autoprefixer');
const sass = require('gulp-ruby-sass');

// scripts
const uglify = require('gulp-uglifyjs');

// other
const concat = require('gulp-concat');
const rimraf = require('gulp-rimraf');
const notify = require('gulp-notify');
const livereload = require('gulp-livereload');

// paths to assets
const paths = {
    dist: 'app/static/public',
    styles: [
        'app/static/sass/**/*.scss',
    ],
    scripts: [
        'app/static/js/**/*.js',
    ],
    images: [
        'app/static/images/*'
    ],
    fonts: [
        'app/static/fonts/*'
    ]
};

// clean out old styles build
gulp.task('clean', () => {
  gulp.src('app/static/public/*')
    .pipe(rimraf());
  return;
});

// SCSS
gulp.task('styles', () => {
  sass(paths.styles)
    .on('error', sass.logError)
    .pipe(autoprefixer('last 2 versions'))
    .pipe(concat('styles.css'))
    .pipe(minifycss({ removeEmpty: true }))
    .pipe(gulp.dest(paths.dist))
    .pipe(livereload())
    .pipe(notify({ message: 'styles built' }));
  return;
});

// JS
gulp.task('scripts', function() {
  return gulp.src(paths.scripts)
    .pipe(concat('app.js'))
    .pipe(uglify())
    .pipe(gulp.dest(paths.dist))
    .pipe(livereload())
    .pipe(notify({ message: 'scripts built' }));
});

// move & compress images
gulp.task('images', () => {
  return gulp.src(paths.images)
    .pipe(gulp.dest(paths.dist))
    .pipe(notify({ message: 'images built'}));
});

// move fonts
gulp.task('fonts', function() {
  return gulp.src(paths.fonts)
    .pipe(gulp.dest(paths.dist))
    .pipe(notify({ message: 'fonts built' }));
});

// file watchers
gulp.task('watch', function() {
  gulp.watch(paths.styles, ['styles']);
  gulp.watch(paths.scripts, ['scripts']);
  gulp.watch(paths.images, ['images']);
  gulp.watch(paths.fonts, ['fonts']);
});

// default
gulp.task('default', ['clean', 'styles', 'scripts', 'images', 'fonts']);