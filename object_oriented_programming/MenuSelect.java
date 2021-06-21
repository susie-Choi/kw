import java.util.ArrayList;

public class MenuSelect {
	private static MenuSelect instance = null;

	// ContactVO와 마찬가지로 생성자 추가할것...

	private MenuSelect() {
	}

	public static MenuSelect getInstance() {
		if (instance == null) {
			instance = new MenuSelect();
		}
		return instance;
	}

	private ArrayList<People> list = new ArrayList<>();

	public int insert(People vo) {
		list.add(vo);
		return 1;
	}

	public ArrayList<People> select() {
		return list;
	}

	public People select(int index) {
		return list.get(index);
	}

	public int delete(int index) {
		list.remove(index);
		return 1;
	}
}
