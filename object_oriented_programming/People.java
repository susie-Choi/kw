public class People {
	// ������ �߰��� ��.
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
		String str = "�̸�" + name + "\n" + "����ó" + phone + "\n";

		return str;
	}
}
