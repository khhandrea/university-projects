import 'package:daily_diet_date/profile.dart';
import 'package:daily_diet_date/sign_up.dart';
import 'package:daily_diet_date/view_profile.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class SignIn extends StatelessWidget {
  const SignIn({super.key});
  static const routeName = '/sign_in';

  @override
  Widget build(BuildContext context) {

    Widget getLoginInfoSection = Card(
      margin: const EdgeInsets.fromLTRB(15, 20, 15, 20),
      elevation: 0,
      child: Column(
        children: [
          Expanded(
            flex: 2,
            child: Column(
              children: [
                Expanded(
                  flex: 5,
                  child: Container(
                    margin: const EdgeInsets.all(10),
                    child: CircleAvatar(
                      backgroundColor: Colors.grey[200],
                      radius: 60,
                      child: const Icon(
                        Icons.person,
                        color: Colors.grey,
                        size: 80,
                      ),
                    ),
                  )
                ),
                Expanded(
                    flex: 2,
                    child: Container(
                      margin: const EdgeInsets.all(10),
                      child: Text(
                        "Please enter your details",
                        style: TextStyle(
                          color: Colors.green.shade500,
                          fontWeight: FontWeight.bold,
                          fontSize: 20,
                        ),
                      )
                    )
                )
              ],
            )
          ),
          Expanded(
            flex: 3,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                _loginInfo("Use Name"),
                _loginInfo("Password"),
                _loginButton(context),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Text(
                      "Don't have an account?",
                      style: TextStyle(
                        color: Colors.green,
                        fontSize: 17,
                      ),
                    ),
                    TextButton(
                      onPressed: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) => const SignUp()
                          )
                        );
                      },
                      child: const Text(
                        "Sign up",
                        style: TextStyle(
                          color: Colors.green,
                          fontSize: 17,
                          decoration: TextDecoration.underline
                        ),
                      )
                    )
                  ]
                )
              ],
            ),
          )
        ],
      ),
    );

    return AnnotatedRegion<SystemUiOverlayStyle>(
      value: SystemUiOverlayStyle.dark,
      child: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [ Colors.white, Colors.green.shade200 ]
          ),
        ),
        child: SafeArea(
          child: Column(
            children: [
              Expanded(
                flex: 1,
                child: Container(
                  decoration: const BoxDecoration(
                    image: DecorationImage(
                      image: AssetImage('assets/robot-lookDown.png'),
                      // fit: BoxFit.cover
                    )
                  )
                )
              ),
              Expanded(
                flex: 5,
                child: Container(
                  margin: const EdgeInsets.fromLTRB(20, 0, 20, 170),
                  height: double.infinity,
                  width: double.infinity,
                  decoration: const BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.all(Radius.circular(8)),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.grey,
                        spreadRadius: 1,
                        blurRadius: 3,
                        offset: Offset(0, 3),
                      )
                    ]
                  ),
                  child: getLoginInfoSection,
                ),
              )
            ],
          )
        ),
      ),
    );
  }

  TextField _loginInfo(String label) {
    return TextField(
      decoration: InputDecoration(
        enabledBorder: const OutlineInputBorder(
          borderSide: BorderSide(
            width: 1, color: Colors.lightGreen,
          ),
          borderRadius: BorderRadius.all(Radius.circular(10)),
        ),
        focusedBorder: const OutlineInputBorder(
          borderSide: BorderSide(
            width: 1, color: Colors.green,
          ),
          borderRadius: BorderRadius.all(Radius.circular(10)),
        ),
        labelText: label,
      ),
    );
  }

  ElevatedButton _loginButton(BuildContext context) {
    return ElevatedButton(
      style: ButtonStyle(
          foregroundColor: const MaterialStatePropertyAll(Colors.white),
          backgroundColor: MaterialStatePropertyAll(Colors.green.shade300),
          fixedSize: const MaterialStatePropertyAll(Size(210, 50)),
          elevation: const MaterialStatePropertyAll(3)
      ),
      onPressed: () {
      },
      child: const Text(
        "Login",
        style: TextStyle(
          fontSize: 20,
          fontWeight: FontWeight.bold
        ),
      ),
    );
  }
}