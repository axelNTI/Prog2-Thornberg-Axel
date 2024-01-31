
// TimeStampedVariable.java
import java.util.Date;

public class TimeStampedVariable<T> {
    protected T variable;
    protected Date timeStamp;

    public TimeStampedVariable(T indata) {
        variable = indata;
        timeStamp = new Date(); // sätter timeStamp till tiden då kodraden körs
    }

    public void updateVariable(T nyaVardet) {
        variable = nyaVardet;
        timeStamp = new Date(); // sätter timeStamp till tiden då kodraden körs
    }

    public Date getTimeStamp() {
        return timeStamp;
    }

    public void printVariable() {
        System.out.println(variable.toString());
    }
}
