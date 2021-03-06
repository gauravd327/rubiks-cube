from cuboid import Cuboid

class Cube():
    def __init__(self, size):
        self.size = size
        self.cube = []
        for x in range(6):
            face = []
            for y in range(3):
                row = []
                for z in range(3):
                    col = ["orange", "green", "red", "blue", "yellow", "white"]
                    row.append(Cuboid(col[x]))


                face.append(row)
            
            self.cube.append(face)


    def getCube(self):
        return self.cube


    def rotate(self, sequence):
        sequence == sequence.upper()
        for i in range(len(sequence)):
            if(sequence[i : i + 2] == "R'"):
                self.rotateR(sequence[i : i + 2], self.getCube())

            elif(sequence[i : i + 2] == "R2"):
                self.rotateR(sequence[i], self.getCube())
                self.rotateR(sequence[i], self.getCube())

            elif(sequence[i] == "R"):
                self.rotateR(sequence[i], self.getCube())

            elif(sequence[i : i + 2] == "L'"):
                self.rotateL(sequence[i : i + 2], self.getCube())

            elif(sequence[i : i + 2] == "L2"):
                self.rotateL(sequence[i], self.getCube())
                self.rotateL(sequence[i], self.getCube())

            elif(sequence[i] == "L"):
                self.rotateL(sequence[i], self.getCube())
            
            elif(sequence[i : i + 2] == "U'"):
                self.rotateU(sequence[i : i + 2], self.getCube())

            elif(sequence[i : i + 2] == "U2"):
                self.rotateU(sequence[i], self.getCube())
                self.rotateU(sequence[i], self.getCube())

            elif(sequence[i] == "U"):
                self.rotateU(sequence[i], self.getCube())

            elif(sequence[i : i + 2] == "D'"):
                self.rotateD(sequence[i : i + 2], self.getCube())

            elif(sequence[i : i + 2] == "D2"):
                self.rotateD(sequence[i], self.getCube())
                self.rotateD(sequence[i], self.getCube())

            elif(sequence[i] == "D"):
                self.rotateD(sequence[i], self.getCube())

            elif(sequence[i : i + 2] == "F'"):
                self.rotateF(sequence[i : i + 2], self.getCube())

            elif(sequence[i : i + 2] == "F2"):
                self.rotateF(sequence[i], self.getCube())
                self.rotateF(sequence[i], self.getCube())

            elif(sequence[i] == "F"):
                self.rotateF(sequence[i], self.getCube())

            elif(sequence[i : i + 2] == "B'"):
                self.rotateB(sequence[i : i + 2], self.getCube())

            elif(sequence[i : i + 2] == "B2"):
                self.rotateB(sequence[i], self.getCube())
                self.rotateB(sequence[i], self.getCube())

            elif(sequence[i] == "B"):
                self.rotateB(sequence[i], self.getCube())

            elif(sequence[i : i + 2] == "M'"):
                self.rotateM(sequence[i : i + 2], self.getCube())


            elif(sequence[i : i + 2] == "M2"):
                self.rotateM(sequence[i], self.getCube())
                self.rotateM(sequence[i], self.getCube())

            elif(sequence[i] == "M"):
                self.rotateB(sequence[i], self.getCube())


    def rotateFaceClockwise(self, mat, N):
        # Transpose the matrix
        for i in range(N):
            for j in range(i):
                temp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp
    
        # swap columns
        for i in range(N):
            for j in range(N // 2):
                temp = mat[i][j]
                mat[i][j] = mat[i][N - j - 1]
                mat[i][N - j - 1] = temp

            
    def rotateFaceAntiClockwise(self, mat, N):
        # Transpose the matrix
        for i in range(N):
            for j in range(i):
                # swap `mat[i][j]` with `mat[j][i]`
                temp = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = temp
    
        # swap rows
        for i in range(N // 2):
            for j in range(N):
                # swap `mat[i][j]` with `mat[N-i-1][j]`
                temp = mat[i][j]
                mat[i][j] = mat[N - i - 1][j]
                mat[N - i - 1][j] = temp    


    def rotateR(self, rotation, total):
        if(rotation == "R"):
            ext = [total[3][0][0].getColor(), total[3][0][1].getColor(), total[3][0][2].getColor()]
            for i in range(3):
                total[3][0][i].setColor(total[5][2][2 - i].getColor())
            
            for i in range(3):
                total[5][2][i].setColor(total[1][2][i].getColor())

            for i in range(3):
                total[1][2][i].setColor(total[4][2][i].getColor())
            
            for i in range(3):
                total[4][2][i].setColor(ext[2 - i])
                

            self.rotateFaceAntiClockwise(total[2], 3)
            

        else:
            ext = [total[1][2][0].getColor(), total[1][2][1].getColor(), total[1][2][2].getColor()]
            for i in range(3):
                total[1][2][i].setColor(total[5][2][i].getColor())      


            for i in range(3):
                total[5][2][i].setColor(total[3][0][2 - i].getColor())


            for i in range(3):
                total[3][0][i].setColor(total[4][2][2 - i].getColor())
              
            for i in range(3):
                total[4][2][i].setColor(ext[i])


            self.rotateFaceClockwise(total[2], 3)



    def rotateL(self, rotation, total):
        if(rotation == "L"):
            ext = [total[1][0][0].getColor(), total[1][0][1].getColor(), total[1][0][2].getColor()]
            for i in range(3):
                total[1][0][i].setColor(total[5][0][i].getColor())      


            for i in range(3):
                total[5][0][i].setColor(total[3][2][2 - i].getColor())


            for i in range(3):
                total[3][2][i].setColor(total[4][0][2 - i].getColor())
              
            for i in range(3):
                total[4][0][i].setColor(ext[i])
            
            self.rotateFaceAntiClockwise(total[0], 3)


        else:
            ext = [total[3][2][0].getColor(), total[3][2][1].getColor(), total[3][2][2].getColor()]
            for i in range(3):
                total[3][2][i].setColor(total[5][0][2 - i].getColor())
            
            for i in range(3):
                total[5][0][i].setColor(total[1][0][i].getColor())

            for i in range(3):
                total[1][0][i].setColor(total[4][0][i].getColor())
            
            for i in range(3):
                total[4][0][i].setColor(ext[2 - i])

            
            self.rotateFaceClockwise(total[0], 3)




    def rotateU(self, rotation, total):
        if(rotation == "U"):
            ext = [total[2][0][0].getColor(), total[2][1][0].getColor(), total[2][2][0].getColor()]
            for i in range(3):       
                total[2][i][0].setColor(total[3][i][0].getColor())  
            
            for i in range(3):
                total[3][i][0].setColor(total[0][i][0].getColor())

            for i in range(3):
                total[0][i][0].setColor(total[1][i][0].getColor())

            for i in range(3):
                total[1][i][0].setColor(ext[i])

            self.rotateFaceAntiClockwise(total[5], 3)


        else:
            ext = [total[0][0][0].getColor(), total[0][1][0].getColor(), total[0][2][0].getColor()]
            for i in range(3):
                total[0][i][0].setColor(total[3][i][0].getColor())  
            
            for i in range(3):
                total[3][i][0].setColor(total[2][i][0].getColor())
            
            for i in range(3):
                total[2][i][0].setColor(total[1][i][0].getColor())
            
            for i in range(3):
                total[1][i][0].setColor(ext[i])

            self.rotateFaceClockwise(total[5], 3)





    def rotateD(self, rotation, total):
        if(rotation == "D"):
            ext = [total[0][0][2].getColor(), total[0][1][2].getColor(), total[0][2][2].getColor()]
            for i in range(3):
                total[0][i][2].setColor(total[3][i][2].getColor())  
            
            for i in range(3):
                total[3][i][2].setColor(total[2][i][2].getColor())
            
            for i in range(3):
                total[2][i][2].setColor(total[1][i][2].getColor())
            
            for i in range(3):
                total[1][i][2].setColor(ext[i])

            self.rotateFaceAntiClockwise(total[4], 3)

        else:
            ext = [total[2][0][2].getColor(), total[2][1][2].getColor(), total[2][2][2].getColor()]
            for i in range(3):       
                total[2][i][2].setColor(total[3][i][2].getColor())  
            
            for i in range(3):
                total[3][i][2].setColor(total[0][i][2].getColor())

            for i in range(3):
                total[0][i][2].setColor(total[1][i][2].getColor())

            for i in range(3):
                total[1][i][2].setColor(ext[i])

            self.rotateFaceClockwise(total[4], 3)






    def rotateF(self, rotation, total):
        if(rotation == "F"):
            ext = [total[2][0][0].getColor(), total[2][0][1].getColor(), total[2][0][2].getColor()]
            for i in range(3):
                total[2][0][i].setColor(total[5][i][2].getColor())

            for i in range(3):       
                total[5][i][2].setColor(total[0][2][2 - i].getColor())  
                

            for i in range(3):
                total[0][2][i].setColor(total[4][i][0].getColor())   


            for i in range(3):
                total[4][2 - i][0].setColor(ext[i])
            

            self.rotateFaceAntiClockwise(total[1], 3)

        else:
            ext = [total[0][2][0].getColor(), total[0][2][1].getColor(), total[0][2][2].getColor()]
            for i in range(3):
                total[0][2][2 - i].setColor(total[5][i][2].getColor())

            for i in range(3):       
                total[5][i][2].setColor(total[2][0][i].getColor())  
                

            for i in range(3):
                total[2][0][2 - i].setColor(total[4][i][0].getColor())   


            for i in range(3):
                total[4][i][0].setColor(ext[i])

            self.rotateFaceClockwise(total[1], 3)







    def rotateB(self, rotation, total):
        if(rotation == "B"):
            ext = [total[0][0][0].getColor(), total[0][0][1].getColor(), total[0][0][2].getColor()]
            for i in range(3):
                total[0][0][2 - i].setColor(total[5][i][0].getColor())

            for i in range(3):       
                total[5][i][0].setColor(total[2][2][i].getColor())  
                

            for i in range(3):
                total[2][2][2 - i].setColor(total[4][i][2].getColor())   


            for i in range(3):
                total[4][i][2].setColor(ext[i])
            

            self.rotateFaceAntiClockwise(total[3], 3)

            


        else:
            ext = [total[2][2][0].getColor(), total[2][2][1].getColor(), total[2][2][2].getColor()]
            for i in range(3):
                total[2][2][i].setColor(total[5][i][0].getColor())

            for i in range(3):       
                total[5][2 - i][0].setColor(total[0][0][i].getColor())  
                

            for i in range(3):
                total[0][0][i].setColor(total[4][i][2].getColor())   


            for i in range(3):
                total[4][2 - i][2].setColor(ext[i])

            self.rotateFaceClockwise(total[3], 3)

        


    def rotateM(self, rotation, total):
        if(rotation == "M"):
            ext = [total[3][1][0].getColor(), total[3][1][1].getColor(), total[3][1][2].getColor()]
            for i in range(3):
                total[3][1][i].setColor(total[5][1][2 - i].getColor())
            
            for i in range(3):
                total[5][1][i].setColor(total[1][1][i].getColor())

            for i in range(3):
                total[1][1][i].setColor(total[4][1][i].getColor())
            
            for i in range(3):
                total[4][1][i].setColor(ext[2 - i])
                
            

        else:
            ext = [total[1][1][0].getColor(), total[1][1][1].getColor(), total[1][1][2].getColor()]
            for i in range(3):
                total[1][1][i].setColor(total[5][1][i].getColor())      


            for i in range(3):
                total[5][1][i].setColor(total[3][1][2 - i].getColor())


            for i in range(3):
                total[3][1][i].setColor(total[4][1][2 - i].getColor())
              
            for i in range(3):
                total[4][1][i].setColor(ext[i])

