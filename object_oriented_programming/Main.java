import java.util.Scanner;

public class Main {

	private static Scanner sc;
	private static MenuSelect ms;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("������б� ���������к� 2017204081 �ּ����� ������Ʈ�Դϴ�.");

		boolean run = true;
		sc = new Scanner(System.in);
		ms = MenuSelect.getInstance();

		while (run) {
			showMainMenu();
			try {
				int select = sc.nextInt();
			} catch (Exception e) {
				System.out.println("�ٽ� �Է����ּ���!"); // ���� �Է��� �ƴ� ��� ����ó��
			} finally {
				System.out.print("1|2|3|4 �� �Է� ���ּ��� : "); // ���� ó���� ���� �ѹ� �� �Է��ϱ�
				int select = sc.nextInt();
				switch (select) {
				case Menu.QUIT:
					run = false;
					System.out.println("���α׷��� �����մϴ�.");
					break;

				case Menu.INSERT:
					insertContact();
					break;

				case Menu.SELECT_ALL:
					selectAllContact();
					break;

				case Menu.DELETE:
					deleteIndexContact();
					break;

				default:
					System.out.println("�������� �����ϴ�. �ٽ� ����ּ���.");
				}
			}
		}
		sc.close();
	}

	static void showMainMenu() { // �޴�
		System.out.println();
		System.out.println("�� �ּҷ� ");
		System.out.println("[1:��� | 2:���� | 3:��ü�˻� | 4:����]");
		System.out.print("���ϴ� ��ȣ�� ����ּ��� : ");
	}

	static void insertContact() { // ���
		System.out.println();
		System.out.println("[���]");

		System.out.print("�̸��� �Է� ���ּ��� : ");
		String name = sc.next();

		System.out.print("����ó�� �Է� ���ּ��� : ");
		String phone = sc.next();

		People contact = new People(name, phone);

		int result = ms.insert(contact);

		if (result > 0) {
			System.out.println("��� ����");
		} else {
			System.out.println("��� ����");
		}
	}

	static void selectAllContact() { // ��ü ����ó
		if (ms.select().isEmpty()) {
			System.out.println("���� ����ó ���ο� �����Ͱ� �����ϴ�.");
		} else {
			System.out.println("��ü ����ó ���");
			for (People num : ms.select()) {
				System.out.print(ms.select().indexOf(num) + " ");
				System.out.println(num);
			}
		}
	}

	static void deleteIndexContact() { // ����ó �����
		if (ms.select().isEmpty()) {
			System.out.println("���� ����ó ���ο� �����Ͱ� �����ϴ�.");
		} else {
			System.out.println();
			System.out.print("������ ����� ��ȣ�� �Է����ּ��� : ");
			int index = sc.nextInt();
			sc.next();

			if (index < ms.select().size()) {
				if (index > 0) {
					int result = ms.delete(index);
					System.out.println("�����Ǿ����ϴ�.");
				} else
					System.out.println("�ٽ� �õ����ּ���.");
			} else {
				System.out.println("�ٽ� �õ����ּ���");
			}
		}
	}
}