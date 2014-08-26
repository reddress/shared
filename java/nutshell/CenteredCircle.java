public class CenteredCircle extends Circle implements Centered {
    protected double cx, cy;
    
    public CenteredCircle(double cx, double cy, double r) {
        super(r);
        this.cx = cx;
        this.cy = cy;
    }

    public void setCenter(double cx, double cy) {
        this.cx = cx;
        this.cy = cy;
    }

    public double getCenterX() {
        return cx;
    }

    public double getCenterY() {
        return cy;
    }
}
