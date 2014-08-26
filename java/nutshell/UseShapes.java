import java.util.*;
import java.io.*;

import static util.Convenience.print;

class UseShapes {
    public static void main(String[] args) {
        Shape[] shapes = new Shape[3];

        shapes[0] = new CenteredCircle(1.0, 1.0, 1.0);
        shapes[1] = new CenteredSquare(2.5, 2, 3);
        shapes[2] = new CenteredRectangle(2.3, 4.5, 3, 4);

        double totalArea = 0;
        double totalDistance = 0;
        for (int i = 0; i < shapes.length; i++) {
            totalArea += shapes[i].area();
            print("shape cx " + ((Centered) shapes[i]).getCenterX());
            if (shapes[i] instanceof Centered) {
                Centered c = (Centered) shapes[i];
                double cx = c.getCenterX();
                double cy = c.getCenterY();
                totalDistance += Math.sqrt(cx * cx + cy * cy);
            }
        }
        print("avg area " + totalArea/shapes.length);
        print("avg dist " + totalDistance/shapes.length);
    }
}
