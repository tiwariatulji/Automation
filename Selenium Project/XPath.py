# ** X Path in Selenium Webdriver
# FROM                                        SYNTAX
# Attribute & Value                          //tagname[@attribute = ‘value’]
# 2 Attributes & Values                      //tagname[@attribute1 = ‘value1’ and/or @attribute2 = ‘value2’]
# Text                                       //tagname[text() = ‘type text here’]
# Starts with                                //tagname[starts-with(@attribute,’starting values’)]
# contains                                   //tagname[contains(@attribute,’value’)]
# Starts with and contains                   //tagname[starts-with(@attribute1,'starting values') and/or contains(@attribute2,’value')]
# Partial Text                              //tagname[contains/starts-with(text(), ‘partial text here’)]

# -----------------------------------------------------------------------------------
                                  
# Parents to any child or grandchild         //tagname[@attribute = ‘value’]//tagname[@attribute = ‘value’]
# Parents to specific no. of child           (//tagname[@attribute = ‘value’]//tagname)[number]
# or grandchild 
# Parents to last child or grandchild        (//tagname[@attribute = ‘value’]//tagname)[last()]
# Parents to 3rd last child or grandchild    (//tagname[@attribute = ‘value’]//tagname)[last()-2]
# Child to any ancestor                      //tagname[@attribute = ‘value’]/ancestor::tagname[@attribute = ‘value’]
# Parent to first n number of child         (//tagname[@attribute = ‘value’]//tagname)[position() >,<,= number]
