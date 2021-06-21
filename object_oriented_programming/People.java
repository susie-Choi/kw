public class People {
	// 생성자 추가할 것.
	private String name;
	private String phone;

	public People() {
	}

	public People(String name, String phone) {
		this.name = name;
		this.phone = phone;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	public String toString() {
		String str = "이름" + name + "\n" + "연락처" + phone + "\n";

		return str;
	}
}
