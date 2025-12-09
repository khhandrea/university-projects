import 'package:flutter/material.dart';
import 'package:flutter/gestures.dart';
import 'dart:ui';
import 'package:google_fonts/google_fonts.dart';
import 'home.dart';


class Social extends StatelessWidget {
  static const routeName = '/social_system';

  const Social({super.key});

  @override
  Widget build(BuildContext context) {
    double baseWidth = 390;
    double fem = MediaQuery.of(context).size.width / baseWidth;
    double ffem = fem * 0.97;
    return Scaffold(
      body: SingleChildScrollView(
        child: Container(
          width: double.infinity,
          child: Container(
            // iphone141HHg (4:6)
            padding: EdgeInsets.fromLTRB(0 * fem, 0 * fem, 0 * fem, 45 * fem),
            width: double.infinity,
            decoration: BoxDecoration(
              color: const Color(0xffffffff),
              borderRadius: BorderRadius.circular(40 * fem),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                SizedBox(
                  // autogroupshjdgj8 (38aGQHfiVRgAjK38v2sHJd)
                  width: double.infinity,
                  height: 731 * fem,
                  child: Stack(
                    children: [
                      Positioned(
                        // maskgroupb5Q (1:23)
                        left: 17 * fem,
                        top: 156 * fem,
                        child: Align(
                          child: SizedBox(
                            width: 355 * fem,
                            height: 575 * fem,
                            child: Image.asset(
                              'assets/mask-group.png',
                              width: 355 * fem,
                              height: 575 * fem,
                            ),
                          ),
                        ),
                      ),
                      Positioned(
                        // ellipse179Uez (1:64)
                        left: 326 * fem,
                        top: 654 * fem,
                        child: Align(
                          child: SizedBox(
                            width: 55 * fem,
                            height: 55 * fem,
                            child: Container(
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(27.5 * fem),
                                color: const Color(0xff88ca5e),
                                boxShadow: [
                                  BoxShadow(
                                    color: const Color(0x3f000000),
                                    offset: Offset(0 * fem, 4 * fem),
                                    blurRadius: 2 * fem,
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ),
                      ),
                      Positioned(
                        // vectoriZL (1:66)
                        left: 341 * fem,
                        top: 668 * fem,
                        child: Align(
                          child: SizedBox(
                            width: 27 * fem,
                            height: 27 * fem,
                            child: Image.asset(
                              'assets/vector.png',
                              width: 27 * fem,
                              height: 27 * fem,
                            ),
                          ),
                        ),
                      ),
                      Positioned(
                        // rectangle3058QSA (4:7)
                        left: 0 * fem,
                        top: 0 * fem,
                        child: Align(
                          child: SizedBox(
                            width: 390 * fem,
                            height: 157 * fem,
                            child: Container(
                              decoration: BoxDecoration(
                                border:
                                    Border.all(color: const Color(0xff000000)),
                                color: const Color(0xff88ca5e),
                                boxShadow: [
                                  BoxShadow(
                                    color: const Color(0x3f000000),
                                    offset: Offset(0 * fem, 4 * fem),
                                    blurRadius: 2 * fem,
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ),
                      ),
                      Positioned(
                        // group324Fp (1:61)
                        left: 322 * fem,
                        top: 91 * fem,
                        child: Container(
                          padding: EdgeInsets.fromLTRB(
                              18.79 * fem, 13 * fem, 25.21 * fem, 14 * fem),
                          width: 64 * fem,
                          height: 43 * fem,
                          decoration: BoxDecoration(
                            color: const Color(0x3f156348),
                            borderRadius: BorderRadius.only(
                              topLeft: Radius.circular(22 * fem),
                              bottomRight: Radius.circular(22 * fem),
                            ),
                          ),
                          child: Center(
  child: GestureDetector(
    onTap: () {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => const Scene()),
      );
    },
    child: SizedBox(
      width: 20 * fem,
      height: 16 * fem,
      child: Image.asset(
        'assets/icarrowback24px.png',
        width: 20 * fem,
        height: 16 * fem,
      ),
    ),
  ),
),

                        ),
                      ),
                      Positioned(
                        // welcomedavidkimJC6 (1:17)
                        left: 89 * fem,
                        top: 88 * fem,
                        child: Align(
                          child: SizedBox(
                            width: 61 * fem,
                            height: 30 * fem,
                            child: Text(
                              'Social',
                              style: GoogleFonts.poppins(
                                fontSize: 20 * ffem,
                                fontWeight: FontWeight.w500,
                                height: 1.5 * ffem / fem,
                                color: Color(0xffffffff),
                              ),
                            ),
                          ),
                        ),
                      ),
                      Positioned(
                        // avatarKcz (1:18)
                        left: 17 * fem,
                        top: 79 * fem,
                        child: Align(
                          child: SizedBox(
                            width: 47 * fem,
                            height: 47 * fem,
                            child: Image.asset(
                              'assets/avatar.png',
                              width: 47 * fem,
                              height: 47 * fem,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                Container(
                  // autogroupft3xpZk (38aGjCHsubL8R2chUYft3X)
                  margin:
                      EdgeInsets.fromLTRB(17 * fem, 0 * fem, 18 * fem, 0 * fem),
                  padding: EdgeInsets.fromLTRB(
                      38 * fem, 23 * fem, 92 * fem, 14 * fem),
                  width: double.infinity,
                  decoration: BoxDecoration(
                    color: const Color(0xffffffff),
                    borderRadius: BorderRadius.circular(34 * fem),
                    boxShadow: [
                      BoxShadow(
                        color: const Color(0x1c23bcc1),
                        offset: Offset(0 * fem, 3 * fem),
                        blurRadius: 1.5 * fem,
                      ),
                    ],
                  ),
                  child: Row(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      Container(
                        // image221HTL (1:20)
                        margin: EdgeInsets.fromLTRB(
                            0 * fem, 0 * fem, 33 * fem, 0 * fem),
                        width: 21 * fem,
                        height: 31 * fem,
                        child: Image.asset(
                          'assets/image-221-D6v.png',
                          fit: BoxFit.cover,
                        ),
                      ),
                      Container(
                        // taptoconnectapplewatchQH4 (1:16)
                        margin: EdgeInsets.fromLTRB(
                            0 * fem, 1 * fem, 0 * fem, 0 * fem),
                        child: Text(
                          'Social',
                          style: GoogleFonts.poppins(
                            fontSize: 12 * ffem,
                            fontWeight: FontWeight.w400,
                            height: 1.5 * ffem / fem,
                            color: Color(0xffcacaca),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
