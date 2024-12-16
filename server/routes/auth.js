const trueLogin = "123@m.r";
const truePass = "12345";

function Validate(req,res) {
    const login = req.body.email;
    const password = req.body.password;

    if (login===trueLogin && password===truePass){
        res.render('afteraut');
        res.redirect(200,"/main");
    }
}

const auth = (app) => {
    app.post('/auth',Validate);
} 

module.exports = auth;