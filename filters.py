#Here
#alston
def tieDye(new_image):

      for x in range (len(new_image)):

          for y in range (len(new_image)):

              h,i,j = new_image[x][y][0],new_image[x][y][1],new_image[x][y][2]
      
              a,b,c = new_image[x][y][0],new_image[x][y][1],new_image[x][y][2]
              average =(a + b + c) / 3

              if h > average:
                h = 255                
              elif h < average:
                h = average
              if i > average:
                i = 255                
              elif i < average:
                i = average                
              if j > average:
                j = 255                
              elif j < average:
                j = average     
      index =((h),(i),(j))      
      new_image[x][y] = index
      
  return new_image
  
#Alston
  
  def BlackandWhite(refImage):
    
  for x in range (len(refImage)):

    for y in range (len(refImage)):

        index = refImage[x][y]
        a,b,c = refImage[x][y][0],refImage[x][y][1],refImage[x][y][2]

        average =(a + b + c) / 3

        index =(average,average,average)

        refImage[x][y] = index
    return refImage


  #Alston
def crayon(new_image):

  test = 0 

    
  for x in range (len(new_image)):
    for y in range (len(new_image)):
      h,i,j = new_image[x][y][0],new_image[x][y][1],new_image[x][y][2]
      
      a,b,c = new_image[x][y][0],new_image[x][y][1],new_image[x][y][2]
      average =(a + b + c) / 3      
      test = new_image[x-1][y-1][0]
      minusfive = new_image[x][y][0]
      minusfive = minusfive - 5
      plusfive = new_image[x][y][0]
      plusfive = plusfive + 5

      if (test > plusfive) or (test < minusfive):
        new_image[x-1][y-1] = (0,0,0)
              
      
  return new_image

#This filter intensifies the blue.
def whaleBlueFilter(n_img):
        n_img[x][y] = ((n_img[x][y][0])*0)/1, ((n_img[x][y][1]*.4))/1,((n_img[x][y][2])*.7)/1

  return n_img


# This filter lay's a yellow sunlight feel over the image.
def yellowDayFilter(r_img, g_img, b_img):
        n_img[x][y] = ((n_img[x][y][0])*.7)/1, ((n_img[x][y][1])*.6)/1,((n_img[x][y][2])*.003)/1 
  return n_img




#This filter makes the image take on a bluish tinge.
def glacierBlue(r_img, g_img, b_img):
  n_img = b_img
  for x in range(len(r_img)):
      for y in range(len(g_img[0])):
        a,b,c = r_img[x][y]
        d,e,f = g_img[x][y]
        g,h,i = b_img[x][y]
        n_img[x][y] = (a, e,i)

        n_img[x][y] = ((n_img[x][y][0])*.105)/1, ((n_img[x][y][1]*.50))/1,((n_img[x][y][2])*.87)/1
  return n_img


