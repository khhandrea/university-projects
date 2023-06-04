import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class SignUp extends StatelessWidget {
  const SignUp({super.key});
  static const routeName = '/sign_up';

  @override
  Widget build(BuildContext context) {

    Widget getInfoSection = Card(
      margin: const EdgeInsets.fromLTRB(15, 0, 15, 0),
      elevation: 0,
      child: Column(
        children: [
          Expanded(
            flex: 1,
            child: Column(
              children: [
                Expanded(
                  flex: 5,
                  child: CircleAvatar(
                    backgroundColor: Colors.grey[200],
                    radius: 60,
                    child: const Icon(
                      Icons.person,
                      color: Colors.grey,
                      size: 80,
                    ),
                  ),
                ),
                Expanded(
                  flex: 1,
                  child: Text(
                    "Please enter your details",
                    style: TextStyle(
                      color: Colors.green.shade500,
                      fontSize: 20,
                    ),
                  )
                )
              ],
            )
          ),
          Expanded(
            flex: 2,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                _personalDetailInfo("Name"),
                _personalDetailInfo("User Name"),
                _personalDetailInfo("Password"),
                _personalDetailInfo("Age"),
                _personalDetailInfo("Email"),
                _personalDataInfoButton(context),
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
                      fit: BoxFit.fill
                    )
                  )
                )
              ),
              Expanded(
                flex: 5,
                child: Container(
                  margin: const EdgeInsets.fromLTRB(20, 0, 20, 50),
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
                  child: getInfoSection,
                ),
              )
            ],
          )
        )
      ),
    );
  }


  TextField _personalDetailInfo(String label) {
    return TextField(
      decoration: InputDecoration(
        enabledBorder: const OutlineInputBorder(
          borderSide: BorderSide(
            width: 1, color: Colors.lightGreen,
          ),
          borderRadius: BorderRadius.all(Radius.circular(10))
        ),
        focusedBorder: const OutlineInputBorder(
          borderSide: BorderSide(
            width: 1, color: Colors.green,
          ),
          borderRadius: BorderRadius.all(Radius.circular(10))
        ),
        labelText: label,
      ),
    );
  }

  ElevatedButton _personalDataInfoButton(BuildContext context) {
    return ElevatedButton(
      style: ButtonStyle(
        foregroundColor: const MaterialStatePropertyAll(Colors.white),
        backgroundColor: MaterialStatePropertyAll(Colors.green.shade300),
        fixedSize: const MaterialStatePropertyAll(Size(160, 50)),
        elevation: const MaterialStatePropertyAll(3)
      ),
      onPressed: () {
        
      },
      child: const Text(
        "Sign Up",
        style: TextStyle(
          fontSize: 17,
          fontWeight: FontWeight.bold
        ),
      ),
    );
  }
}