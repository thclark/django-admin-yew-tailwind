echo "Building tailwind ($1 mode)"
if [ $1==debug ]
then
   tailwindcss -o ./tailwind.css
else
   NODE_ENV=production tailwindcss -c ./tailwind.config.js -o ./tailwind.css --minify
fi
