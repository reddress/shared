public class CenteredRectangle extends Rectangle implements Centered {
    private double cx, cy;

    public CenteredRectangle(double cx, double cy, double w, double h) {
        super(w, h);
        this.cx = cx;
        this.cy = cy;
    }

    public void setCenter(double x, double y) {
        cx = x;
        cy = y;
    }

    public double getCenterX() {
        return cx;
    }

    public double getCenterY() {
        return cy;
    }
}
