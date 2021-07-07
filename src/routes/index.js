const express = require('express')
const router = express.Router();
//Routes
router.get('/',(req,res)=> {
    //res.sendFile(path.join(__dirname +"/views/index.html"));
    res.render('index.html',{ title: 'Holi' });
    res.render('main.js');

});

router.get('/redirect',(req,res)=> {
    //res.sendFile(path.join(__dirname +"/views/index.html"));
    res.render('redirect.html',{ title: 'Manuel' });
});

module.exports = router;